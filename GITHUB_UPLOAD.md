# GitHub Upload Instructions

Follow these steps to upload your Stack project to GitHub.

## Prerequisites

1. **Install Git**: https://git-scm.com/download/win
2. **Create a GitHub Account**: https://github.com (if you don't have one)
3. **Have your project folder ready**: `c:\Users\kajus\OneDrive\Documents\python`

## Step 1: Initialize a Git Repository

Open PowerShell in your project folder and run:

```powershell
cd "c:\Users\kajus\OneDrive\Documents\python"
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

## Step 2: Create Initial Commit

```powershell
git add .
git commit -m "Initial commit: Stack implementation with OOP principles and Factory pattern"
```

## Step 3: Create GitHub Repository

1. Go to https://github.com/new
2. Enter repository name: `stack-project` (or any name you prefer)
3. Add Description: "A comprehensive Stack data structure implementation demonstrating all four OOP pillars, design patterns, and best practices."
4. Choose Public (so assessors can view it)
5. **Do NOT** initialize with README (you already have one)
6. Click "Create repository"

## Step 4: Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands to run. Copy and adapt the following (replace `YOUR_GITHUB_USERNAME`):

```powershell
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/stack-project.git
git push -u origin main
```

## Step 5: Verify Upload

1. Visit `https://github.com/YOUR_GITHUB_USERNAME/stack-project`
2. Confirm you see:
   - All `.py` files
   - `README.md`
   - `REPORT.md`
   - `.gitignore`

## Using SSH (Optional, for Future Pushes)

For a more secure connection, set up SSH keys:

```powershell
# Generate SSH key (if you don't have one)
ssh-keygen -t ed25519 -C "your.email@example.com"

# Add key to GitHub at https://github.com/settings/keys
cat "c:\Users\kajus\.ssh\id_ed25519.pub" | clip  # Copy to clipboard
```

Then change your remote:

```powershell
git remote set-url origin git@github.com:YOUR_GITHUB_USERNAME/stack-project.git
```

## Making Future Updates

After making changes to your code:

```powershell
git add .
git commit -m "Describe what changed"
git push
```

## Useful Git Commands

```powershell
# Check status
git status

# View commit history
git log --oneline

# View remote URL
git remote -v

# Undo last commit (before pushing)
git reset --soft HEAD~1
```

## Troubleshooting

### Authentication Error
If you get an authentication error, use:
```powershell
git remote set-url origin https://YOUR_GITHUB_USERNAME:YOUR_PERSONAL_ACCESS_TOKEN@github.com/YOUR_GITHUB_USERNAME/stack-project.git
```

Create a Personal Access Token at: https://github.com/settings/tokens

### Files Not Pushing
Make sure files aren't in `.gitignore`:
```powershell
git check-ignore -v filename.py
```

### Large Files
If you accidentally added large files:
```powershell
git rm --cached largefile.csv
git commit -m "Remove large file"
git push
```

---

## GitHub Repository Contents Checklist

Your repository should contain:

✅ **Source Code**
- abstract_stack.py
- stack.py
- bounded_stack.py
- min_stack.py
- node.py
- factory.py
- file_handler.py
- history.py
- operation_record.py
- state.py
- actions_stack.py
- actions_file.py
- helpers.py
- demo.py
- main.py
- test_stack.py

✅ **Documentation**
- README.md (Quick start guide)
- REPORT.md (Detailed coursework report)

✅ **Configuration**
- .gitignore (Excludes Python cache files)

## GitHub Repository Description

Use this in your repository settings:

**Description:**
```
A comprehensive Stack data structure implementation in Python demonstrating all four OOP pillars (Abstraction, Inheritance, Polymorphism, Encapsulation), the Factory Method design pattern, composition and aggregation principles, CSV file I/O, and comprehensive unit testing.
```

**Topics:** Add these tags to your repository for discoverability:
- `object-oriented-programming`
- `design-patterns`
- `factory-method`
- `data-structures`
- `python`
- `unit-testing`
- `coursework`

---

## After Upload

Once uploaded:

1. **Share the link** with your instructor/assessors
2. **Pin the repository** to your GitHub profile for easy access
3. **Consider adding** a GitHub Pages website (optional) using the README.md

---

**Congratulations!** Your Stack project is now on GitHub and ready for review. 🎉
