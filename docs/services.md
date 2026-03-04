# Service Layer

This document describes the service layer of the system.

The service layer contains all business logic.
Domain objects remain pure data structures.

Services are responsible for:

- Managing domain objects
- Executing scheduling logic
- Handling user modifications
- Managing persistence

Each service has a single responsibility.

---

## Design Principles

1. **Separation of concerns**  
   Services handle logic.  
   Domain objects hold data only.

2. **Stateless where possible**  
   Services do not permanently store state.
   State is passed in and returned explicitly.

3. **Clear responsibility boundaries**  
   Each service focuses on one domain area.

---

## PlanningService

Core scheduling engine.

Responsible for generating and re-generating schedules.

### Methods

- `generate_schedule(tasks, exceptions) -> Schedule`
- `replan_from_existing(existing_schedule, tasks, exceptions) -> Schedule`

### Responsibilities

- Convert tasks into atomic time allocations
- Respect `BLOCK` and `LOCK` exceptions
- Ensure each task meets its required hours
- Produce a deterministic scheduling result

This service contains the main planning algorithm.

---

## TaskService

Manages the lifecycle of tasks.

### Methods

- `add_task(task)`
- `update_task(task_id, **fields)`
- `delete_task(task_id)`
- `list_tasks() -> List[Task]`

### Responsibilities

- Create and modify user requirements
- Validate task input
- Provide task collection to the planner

This service does not perform scheduling.

---

## ExceptionService

Handles user intervention on the timeline.

### Methods

- `add_block(start, end)`
- `add_lock(assignment_id)`
- `remove_exception(id)`

### Responsibilities

- Represent blocked time
- Lock specific assignments
- Provide exception data to the planner

Exceptions influence planning but do not execute planning themselves.

---

## ScheduleService

Manages schedule retrieval and export.

### Methods

- `get_current_schedule() -> Schedule`
- `export_to_file(schedule, path)`

### Responsibilities

- Provide access to the latest schedule
- Handle exporting logic
- Coordinate with storage layer

---

## StorageService

Abstract persistence layer.

### Methods

- `save(path)`
- `load(path)`

### Responsibilities

- Save tasks, exceptions, and schedules
- Load existing planning state
- Isolate file format details from core logic

The storage implementation can evolve without affecting domain or planning logic.

---

## Service Interaction Overview

Typical flow:

1. TaskService updates tasks
2. ExceptionService updates timeline constraints
3. PlanningService generates or re-generates schedule
4. ScheduleService provides schedule to UI
5. StorageService saves snapshot

Each service remains independent and composable.