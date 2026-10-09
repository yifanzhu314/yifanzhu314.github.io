# Yifan Zhu — academic homepage

A responsive, static academic site. Research metadata lives in `data/publications.json`; biography and layout live in `data/page.html`. Run the renderer after editing either file. `index.html` is generated and checked in for GitHub Pages and ordinary static hosting.

```sh
python3 scripts/build.py
python3 -m unittest discover -s tests -v
python3 scripts/build.py --check
python3 -m http.server 4395 --bind 127.0.0.1
```

Use a regular Python interpreter if macOS's system Python asks for Xcode setup. No Node or application server is needed. Existing publication illustrations and portrait are retained from this repository.

## Content verification

Reviewed on 2026-10-09 against the owner's [Scholar profile](https://scholar.google.com/citations?user=6abekesAAAAJ) and primary sources linked on the page. Nine distinct works are stored; six selected works are displayed; supplementary material is not counted as a separate paper. Author order follows arXiv/CVF for selected works. Seed3D reports display only the core contributors listed in Appendix A.1, retain the report order, and explicitly note alphabetical ordering by last name. Full author metadata remains stored separately; no first authorship is implied. Older Scholar records retain initials where names were not established. Citation counts are omitted rather than presented as live statistics.

Primary sources: [Seed3D 1.0](https://arxiv.org/abs/2510.19944), [Seed3D 2.0](https://arxiv.org/abs/2605.13862), [CVPR 2023](https://openaccess.thecvf.com/content/CVPR2023/html/Qiu_Looking_Through_the_Glass_Neural_Surface_Reconstruction_Against_High_Specular_CVPR_2023_paper.html), [ICCV 2023](https://openaccess.thecvf.com/content/ICCV2023/html/Cai_Consistent_Depth_Prediction_for_Transparent_Object_Reconstruction_from_RGB-D_Camera_ICCV_2023_paper.html), [ICCV 2021](https://openaccess.thecvf.com/content/ICCV2021/html/Zhu_Transfusion_A_Novel_SLAM_Method_Focused_on_Transparent_Objects_ICCV_2021_paper.html), [RDNeRF](https://ren-bo.net/papers/qjx_tvcj2023_1.pdf), [CVM 2023](https://iccvm.org/2023/papers/poster-9-311.pdf).

## Server hosting

The server serves an immutable release directory through Caddy at the configured homepage domain. Copy only `index.html`, `stylesheet.css`, and `images/`; no credentials, personal database or proxy subscription belong in this public repository. Releases are independent of Data Hub; only the HTTPS gateway is shared. Switch the `current` symlink after validation; return it to the previous release to roll back. TLS and DNS are managed outside this repository. `CNAME` controls GitHub Pages and must match the chosen domain.

This site originated from [Jon Barron's academic site](https://github.com/jonbarron/jonbarron.github.io); the page has been reworked while retaining the owner's supplied imagery.

## Verified deployment (2026-10-09)

Live at https://home.majortom314.com/ on the existing server. Five site tests and the Site checks CI passed. HTTPS HTML, images and styles were inspected; a phone viewport had no horizontal overflow. The existing apex and www DNS records were preserved. This is a deployment snapshot, not continuous monitoring.

## Compact presentation (2026-10-10)

The introduction includes education and current 3D generation work. Navigation, contact buttons, research-direction slogans and additional-work lists are omitted. Seed3D 2.0 uses the cover image from the [official project page](https://seed.bytedance.com/zh/seed3d_2_0), served from the official image CDN; its availability depends on that source. The portrait is 112 pixels on desktop and smaller on phones.

2026-10-10 compact release verified live: six site tests and both Site checks / Pages CI succeeded. Official cover image loaded, desktop portrait is 112px, phone portrait is 64px, and neither viewport overflowed horizontally. Server release: `compact-20261010`; previous release remains available for rollback.

Biography wording updated on 2026-10-10: education precedes current work; Haiyong Chen links to the owner-supplied Google Scholar profile.

Core-contributor groups verified on 2026-10-10 against Appendix A.1 of both technical reports; 15 names per report. The renderer uses the explicit core_contributors field instead of inferring contribution roles from a display name or author count.
