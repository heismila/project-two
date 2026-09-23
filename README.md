# Project Two

A demonstration of a realistic multi-branch Git workflow, including a
deliberate merge conflict and its clean resolution.

## Branching Strategy

This project follows **GitHub Flow**:

- `main` is always deployable and protected.
- Every change starts from a short-lived feature branch named
  `feature/<short-description>`.
- Each feature is merged back to `main` through a **pull request** with a
  descriptive title and body.
- Feature branches are deleted after merge.
- Commit messages follow **Conventional Commits**
  (`feat:`, `fix:`, `docs:`, `chore:`, `merge:`).

## Workflow Diagram

    main ----*--------------*--------------*------------>
             \            / \            /
              \          /   \          /
        feature/auth ---*     \        /
                               \      /
                     feature/data ----*

## Project Layout

    src/                     application source
    tests/                   automated tests
    docs/pull-requests/      PR descriptions and conflict notes

## Setup

    python3 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    