# Solution — M.AI Task Management System

**Result:** Completed Levels 1–3 within ~95 minutes; Level 4 not reached.

---

## Approach

Progressive React component build-out. Each level adds a distinct concern:
- L1: static rendering from JSON
- L2: controlled form with local state
- L3: async data fetching + secondary per-item API calls

The key constraint throughout: CSS class names must match exactly — tests query the DOM by selector.

---

## Level 1 — Static render from JSON

**TaskCard.tsx** — implement the card template:
```tsx
interface TaskCardProps {
  title: string;
  description: string;
}

export const TaskCard: React.FC<TaskCardProps> = ({ title, description }) => (
  <div className="card">
    <h3 className="card__title">{title}</h3>
    <p className="card__description">{description}</p>
  </div>
);
```

**TaskColumn.tsx** — accept a `tasks` prop and map over it:
```tsx
import { TaskCard } from './TaskCard';

interface Task {
  id: string;
  title: string;
  description: string;
}

interface TaskColumnProps {
  title: string;
  tasks: Task[];
}

const TaskColumn: React.FC<TaskColumnProps> = ({ title, tasks }) => (
  <div className="column">
    <h2 className="column__title">{title}</h2>
    <div className="column__cards">
      {tasks.map(task => (
        <TaskCard key={task.id} title={task.title} description={task.description} />
      ))}
    </div>
  </div>
);
```

**App.tsx** — wire up the three columns from JSON:
```tsx
import taskData from './taskData.json';
const { todoItems, inProgressItems, doneItems } = taskData.tasks;

const App: React.FC = () => (
  <main>
    <div className="board">
      <h2 className="board__title">Tasks</h2>
      <div className="board__columns">
        <TaskColumn title="To Do"       tasks={todoItems} />
        <TaskColumn title="In Progress" tasks={inProgressItems} />
        <TaskColumn title="Done"        tasks={doneItems} />
      </div>
    </div>
  </main>
);
```

---

## Level 2 — Create task form

**CreateTaskForm.tsx** — new file, controlled inputs:
```tsx
import { useState } from 'react';
import { v4 as uuidv4 } from 'uuid';

interface Task { id: string; title: string; description: string; }

interface CreateTaskFormProps {
  onAddTask: (task: Task) => void;
}

const CreateTaskForm: React.FC<CreateTaskFormProps> = ({ onAddTask }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!title || !description) return;
    onAddTask({ id: uuidv4(), title, description });
    setTitle('');
    setDescription('');
  };

  return (
    <div className="create-task-form">
      <h2 className="create-task-form__title">Create task</h2>
      <form onSubmit={handleSubmit}>
        <input name="title" placeholder="Title" value={title} onChange={e => setTitle(e.target.value)} />
        <textarea name="description" placeholder="Description" value={description} onChange={e => setDescription(e.target.value)} />
        <input type="submit" value="Add new task" />
      </form>
    </div>
  );
};
```

**App.tsx** — lift todo state, render form above board:
```tsx
import { useState } from 'react';
import CreateTaskForm from './CreateTaskForm';

const App: React.FC = () => {
  const [todoItems, setTodoItems] = useState(taskData.tasks.todoItems);

  return (
    <main>
      <CreateTaskForm onAddTask={task => setTodoItems(prev => [...prev, task])} />
      <div className="board">
        ...
        <TaskColumn title="To Do" tasks={todoItems} />
        ...
      </div>
    </main>
  );
};
```

---

## Level 3 — API + assigned users

Significant re-architecture: tasks now come from a flat API list with a `status` field, and each task may have an `assignedUser` ID requiring a secondary fetch.

**TaskCard.tsx** — add optional `owner` prop:
```tsx
interface TaskCardProps {
  title: string;
  description: string;
  owner?: string;
}

export const TaskCard: React.FC<TaskCardProps> = ({ title, description, owner }) => (
  <div className="card">
    <h3 className="card__title">{title}</h3>
    {owner && <span className="card__owner">Assigned user: {owner}</span>}
    <p className="card__description">{description}</p>
  </div>
);
```

**App.tsx** — fetch tasks, then fan out user fetches:
```tsx
import { useState, useEffect } from 'react';

const TASKS_API = 'https://api-regional.codesignalcontent.com:443/task-management-system/tasks';
const USERS_API = 'https://api-regional.codesignalcontent.com:443/task-management-system/users';

interface ApiTask {
  id: string; title: string; description: string;
  status: 'TO_DO' | 'IN_PROGRESS' | 'DONE';
  assignedUser?: string;
}

interface DisplayTask extends ApiTask { ownerName?: string; }

const App: React.FC = () => {
  const [tasks, setTasks] = useState<DisplayTask[]>([]);

  useEffect(() => {
    fetch(TASKS_API)
      .then(r => r.json())
      .then(async (apiTasks: ApiTask[]) => {
        const withOwners = await Promise.all(
          apiTasks.map(async task => {
            if (!task.assignedUser) return task;
            const res = await fetch(`${USERS_API}/${task.assignedUser}`);
            if (!res.ok) return task;
            const user = await res.json();
            return { ...task, ownerName: user.name };
          })
        );
        setTasks(withOwners);
      });
  }, []);

  const byStatus = (status: string) => tasks.filter(t => t.status === status);

  return (
    <main>
      <CreateTaskForm onAddTask={...} />
      <div className="board">
        <h2 className="board__title">Tasks</h2>
        <div className="board__columns">
          <TaskColumn title="To Do"       tasks={byStatus('TO_DO')} />
          <TaskColumn title="In Progress" tasks={byStatus('IN_PROGRESS')} />
          <TaskColumn title="Done"        tasks={byStatus('DONE')} />
        </div>
      </div>
    </main>
  );
};
```

**TaskColumn.tsx** — pass `owner` through to TaskCard:
```tsx
{tasks.map(task => (
  <TaskCard key={task.id} title={task.title} description={task.description} owner={task.ownerName} />
))}
```

---

## Key Observations

- **CSS selectors are the test surface** — class names like `card__title`, `column__cards`, `create-task-form__title` must be exact. BEM naming is enforced by the test suite, not a style choice.
- **Users API is N+1 by design** — the instructions explicitly say "request items one by one." `Promise.all` parallelizes the fetches without violating this constraint.
- **404 handling is a test case** — silently dropping the user name when the Users API 404s is required behavior, not defensive coding.
- **Form validation is UI-layer only** — empty field check is sufficient; no server-side validation needed.
- **Level 2 state lives in App** — the form needs to push into the same `todoItems` array that the column renders, so state must be lifted.
