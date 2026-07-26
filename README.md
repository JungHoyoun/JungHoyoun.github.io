# Hoyoun Jung CV Site

Personal CV and project site built with Jekyll Chirpy and deployed through GitHub Pages.

## Local Preview

The site is intended to be built by GitHub Actions. For local preview with Ruby installed:

```bash
bundle install
bundle exec jekyll serve
```

## Deployment

Pushing to `main` triggers the GitHub Pages workflow.

## Publishing notes

Blog post sources live in the Obsidian vault under `0. Slip-box/`.
The desktop GitHub Pager plugin publishes approved notes to `_posts/` and
`assets/img/posts/` through the GitHub API. Routine publishing does not use a
permanent local clone of this repository.

Treat generated post files as deployment output. Edit the originating Obsidian
note and republish instead of editing `_posts/` directly.
