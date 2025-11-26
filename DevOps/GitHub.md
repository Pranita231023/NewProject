# 🧑‍💻 Practical 2: Cloning, Branching, Pushing, and Pull Requests on GitHub (updated flow)

## 🧠 What I Learned

Today, I learned how to:

1. **Clone** a GitHub repository to my computer.
2. **Create a new branch first** (work on feature branch locally).
3. **Create or edit files** on that branch.
4. **Add, commit, and push** the branch to GitHub.
5. **Open a Pull Request** to merge into `main`.
6. **Sync changes** from GitHub to my local `main`.
7. **Clear old login information** using Credential Manager.

---

## 🔧 Steps I Did (modified order: create feature branch right after cloning)

### ✅ 1. Clone the Repository from GitHub

```bash
git clone https://github.com/PhapaleSai/College_repo.git
```

👉 Now a folder named `College_repo` is on your computer.

---

### ✅ 2. Enter the Repository

```bash
cd College_repo/
ls
```

This shows the files and folders inside the project.

---

### ✅ 3. Create a New Branch (do this immediately after cloning)

Create and switch to a new branch called `feature`:

```bash
git checkout -b feature
```

🔄 This creates `feature` and checks it out so you’re working on that branch.

---

### ✅ 4. Create or Edit a File on the `feature` Branch

Option A — Use `vim`:

```bash
vim sai.txt
# press i to insert, type your text, Esc, :wq, Enter to save and quit
```

Option B — Use echo:

```bash
echo "hello i am sai" > sai.txt
```

---

### ✅ 5. Check Git Status

```bash
git status
```

See which files are untracked or modified on the `feature` branch.

---

### ✅ 6. Add the File to Staging

```bash
git add sai.txt
# or to add everything: git add .
```

---

### ✅ 7. Commit Your Changes

```bash
git commit -m "Added sai.txt with introduction"
```

This saves a snapshot on the `feature` branch.

---

### ✅ 8. (Optional) Ensure Remote Is Set

If remote isn't set (usually isn't needed after clone), add it:

```bash
git remote add origin https://github.com/PhapaleSai/College_repo.git
git remote -v
```

---

### ✅ 9. Push the `feature` Branch to GitHub

```bash
git push origin feature
```

🚀 Your `feature` branch and commits are now on GitHub.

---

### ✅ 10. Create a Pull Request (on GitHub)

1. Go to: `https://github.com/PhapaleSai/College_repo`
2. Click **Compare & pull request** for the `feature` branch.
3. Add title/description (e.g., "Added sai.txt").
4. Click **Create Pull Request**.
5. When ready, click **Merge pull request** → **Confirm merge**.

🎉 Your changes are now merged into `main` on GitHub.

---

### ✅ 11. Sync Changes from GitHub to Your Local `main`

Switch back to local `main` and pull:

```bash
git checkout main
git pull origin main
```

This updates your local `main` with the merged changes.

---

### ✅ 12. Important Note: Credential Manager (Windows)

If the wrong GitHub credentials are cached:

1. Open **Windows Search** → type **Credential Manager**.
2. Open it → **Windows Credentials**.
3. Remove any entries for `git:https://github.com`.
4. Next push/pull will prompt you for the correct login.

---

## 📌 Summary of Commands (updated order)

```bash
git clone https://github.com/PhapaleSai/College_repo.git
cd College_repo/
git checkout -b feature        # create & switch to feature branch first
# create/edit file:
vim sai.txt                    # or: echo "hello i am sai" > sai.txt
git status
git add sai.txt                # or git add .
git commit -m "Added sai.txt with introduction"
git remote add origin <repo-url>   # only if needed
git remote -v                   # optional check
git push origin feature
# create PR on GitHub, merge into main
git checkout main
git pull origin main
```

---

## 💡 Tips (reminders)

* Creating the branch immediately after cloning keeps your changes isolated and makes collaboration cleaner.
* Use `git status` often.
* Use descriptive commit messages.
* If you need to update the feature branch after creating the PR, make more commits on `feature` and `git push origin feature` — the PR updates automatically.

---
