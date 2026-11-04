# Clarity

> *A minimal, calm 2-pane goals & work manager for the terminal. No bloat, no backlogs. Just focus.*

---

Modern task apps are bloated monstrosities. They demand that you tag, categorize, estimate story points, calculate burndown velocity, and triage a relentless barrage of overdue badges. Before you have written a single line of code or finished a clear thought, you have spent an hour grooming a backlog.

We do not need another Jira. We do not need an Electron wrapper devouring 2 GB of memory just to tell us what to work on next.

**Clarity cuts the crap.**

Clarity is an opinionated, calm, distraction-free terminal tool built on one timeless truth: **You can only make meaningful progress on a handful of major things at a time.**

---

## 💡 The Philosophy

- **Two Panes. That's It.**
  The left pane holds your big ambitions (e.g. *Ship the v1*, *Reclaim Physical Health*, *Study Distributed Systems*). The right pane holds immediate, short-term actions for the active goal. No infinite sub-task nesting. No Gantt charts.
- **Keyboard as an Extension of Thought.**
  Vim-inspired, fluid navigation that gets out of your way. Navigate, reorder, check off, and archive without your fingers ever leaving the home row.
- **Herdr-Style Workspaces.**
  Organize major spheres of your life (*Work*, *Personal*, *Open Source*) across clean window tabs at the top. Focus on one context, without cross-contamination.
- **Respect for Your Machine & Privacy.**
  Zero cloud accounts. Zero tracking or telemetry. No recurring monthly subscription. Boots in milliseconds, renders natively in your Omarchy theme palette (`colors.toml`), and saves atomically to clean local JSON that you actually own.
  - <kbd>↑</kbd> / <kbd>↓</kbd> (or <kbd>j</kbd>/<kbd>k</kbd>) to move inside the active goals or workspace.
  - <kbd>Shift</kbd> + <kbd>↑</kbd> / <kbd>↓</kbd> (or <kbd>K</kbd>/<kbd>J</kbd>) to rearrange items up or down.
  - <kbd>Enter</kbd> to step directly into the goal's workspace.
  - <kbd>Esc</kbd> to exit archive (returns to active goals) or step back out to your major goals.
  - <kbd>Space</kbd> to check off a goal.
  - <kbd>c</kbd> to archive / unarchive a major goal (docks to pure bottom scrollable archive).
  - <kbd>Shift</kbd> + <kbd>c</kbd> (or <kbd>C</kbd>) to jump directly into the bottom archive.
  - <kbd>n</kbd> to create a new goal or step inline.
  - <kbd>e</kbd> to edit.
  - <kbd>d</kbd><kbd>d</kbd> to remove.
  - <kbd>Alt</kbd> + <kbd>1..9</kbd> to jump directly to window tab.
  - <kbd>Alt</kbd> + <kbd>←</kbd> / <kbd>→</kbd> (or <kbd>[</kbd> / <kbd>]</kbd>) to switch window tabs.
  - <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>←</kbd> / <kbd>→</kbd> (or <kbd>Alt</kbd>+<kbd>H</kbd>/<kbd>L</kbd>) to rearrange window tabs.
  - <kbd>Alt</kbd> + <kbd>t</kbd> to create a new window tab.
  - <kbd>Alt</kbd> + <kbd>r</kbd> to rename the active window.
  - <kbd>Alt</kbd> + <kbd>w</kbd> to close the active window.
  - <kbd>?</kbd> to view full keyboard shortcuts cheatsheet.
  - <kbd>q</kbd> to quit.

---

## ⌨️ Controls

| Key | Action | Context |
| :--- | :--- | :--- |
| <kbd>?</kbd> | **Open shortcuts cheatsheet modal** | Anywhere |
| <kbd>↑</kbd> / <kbd>↓</kbd> or <kbd>j</kbd> / <kbd>k</kbd> | Move selection up / down | Active pane |
| <kbd>Shift</kbd> + <kbd>↑</kbd> / <kbd>↓</kbd> or <kbd>K</kbd> / <kbd>J</kbd> | **Rearrange / move item up or down** | Active pane |
| <kbd>Enter</kbd> or <kbd>→</kbd> / <kbd>l</kbd> | **Open Workspace** (step into right pane) | Major Goals pane |
| <kbd>Esc</kbd> | **Exit Archive to Active Goals** or **Back to Goals** from Workspace | Anywhere |
| <kbd>Space</kbd> | Toggle completed (<span style="color:#2a9d8f">✔</span> / <span style="color:#5c5c5c">◻</span>) | Workspace pane |
| <kbd>c</kbd> | **Archive / Unarchive Major Goal** (docks to pure bottom scrollable section) | Major Goals pane |
| <kbd>Shift</kbd> + <kbd>c</kbd> / <kbd>C</kbd> | **Jump focus to / from bottom Archived section** | Major Goals pane |
| <kbd>n</kbd> or <kbd>a</kbd> | Add new item inline | Active pane |
| <kbd>e</kbd> | Edit highlighted item inline | Active pane |
| <kbd>d</kbd><kbd>d</kbd> or <kbd>Delete</kbd> | Delete highlighted item (double-tap <kbd>d</kbd>) | Active pane |
| <kbd>Tab</kbd> | Alternate between panes | Anywhere |
| <kbd>Alt</kbd> + <kbd>t</kbd> / <kbd>Ctrl</kbd> + <kbd>t</kbd> | **New window tab** | Anywhere |
| <kbd>Alt</kbd> + <kbd>1..9</kbd> | Jump directly to window 1..9 | Top tab bar |
| <kbd>Alt</kbd> + <kbd>←</kbd> / <kbd>→</kbd> or <kbd>[</kbd> / <kbd>]</kbd> | Switch previous / next window tab | Anywhere |
| <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>←</kbd> / <kbd>→</kbd> or <kbd>Alt</kbd>+<kbd>H</kbd>/<kbd>L</kbd> | **Rearrange active window tab left / right** | Anywhere |
| <kbd>Alt</kbd> + <kbd>r</kbd> / <kbd>Ctrl</kbd> + <kbd>r</kbd> | **Rename active window tab** | Anywhere |
| <kbd>Alt</kbd> + <kbd>w</kbd> / <kbd>Ctrl</kbd> + <kbd>w</kbd> | **Close active window tab** | Anywhere |
| <kbd>q</kbd> | Quit | Anywhere |

---

## 💾 Storage

Goals are saved automatically and atomically as clean JSON at:
```
~/.local/share/goals/goals.json
```
