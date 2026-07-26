# Homepage operating guide

## Content ownership

- The canonical source for blog posts is the Obsidian vault's `0. Slip-box/`.
- `_posts/` and `assets/img/posts/` are generated publishing output.
- Do not hand-edit a generated post. Update the originating Obsidian note and
  publish it again with GitHub Pager.
- Routine publishing must not depend on a permanent local clone or a resident
  background process.

## Site-code changes

- Use this repository for layouts, navigation, workflows, portfolio assets,
  and other website code.
- Keep unrelated generated posts and images untouched.
- Before removing a post image, verify that no published post references it.
- Validate changes with the Jekyll build and HTML-Proofer workflow.

## Deployment

- Pull requests run the site build and link checks.
- A push to `main` builds and deploys GitHub Pages.
- A failed build must leave the previously deployed site intact.
