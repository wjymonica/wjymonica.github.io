# Jingying Wang’s personal website

A responsive, accessible static academic website. No package installation or build step is required.

## Edit and preview

- `index.html`: biography, news, research, authors, and links.
- `styles.css`: layout, colors, typography, mobile and print styles.
- `img/`: portrait, research figures, and CV (`My_Resume.pdf`).

Run `python3 -m http.server 8000` from the repository, then open http://localhost:8000.
Keep project statuses and academic details up to date when editing. Historical news dates should stay attached to their original events.

## Keep both repositories synchronized

Use `wjymonica/wjymonica.github.io` as the primary editing repository; it matches the GitHub account’s user-site name. Both repositories contain the same shared site files. Their Git histories, repository settings, and legacy Notion exports remain independent.

With both repositories cloned beside each other, edit the primary checkout and compare:

```sh
python3 scripts/sync-site.py ../jingyingwang.github.io
```

Review differences before copying. Copying overwrites matching shared files in the target, so commit or save any target edits first:

```sh
python3 scripts/sync-site.py ../jingyingwang.github.io --apply
python3 scripts/sync-site.py ../jingyingwang.github.io
```

The script copies only the homepage, stylesheet, image directory, synchronization script, `.nojekyll`, and this README. It does not delete target files, copy Git metadata or credentials, push commits, or change hosting settings. Synchronization is manual; run it after each update.

Review and commit the changes in each checkout, then publish both:

```sh
git push origin main
git -C ../jingyingwang.github.io push origin main
```

GitHub Pages must be configured separately in each repository under Settings → Pages, using `main` and the repository root for branch-based publishing. Keep any custom domain configuration specific to its repository.

## Content provenance

Research titles, authors, news, publication links, CV, and figures were retained from the existing site. The year-specific Ph.D. wording was generalized to avoid becoming stale. Unpublished project statuses were retained and should be confirmed by the owner before updating them.
