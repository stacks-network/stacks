# [Blockstack Core](https://github.com/blockstack/blockstack-core) Release Checklist

1. [ ] Run integration tests on the `develop` branch and make sure they are passing
1. [ ] Make some release notes.
  * These live in `blockstack/blockstack-core/release-notes/changelog-x.y.z.md`
1. [ ] Open and merge PR for `develop` -> `master`
1. [ ] Build the documentation with the `blockstack/blockstack-core/build_docs.sh deploy_gh` script in the root of the repo
  * Requires aglio (`npm install -g aglio`)
1. [ ] Push build to `pip`
  * `cd blockstack/blockstack/packaging` and run `make deploy-pypi`
  * Need secrets file at path=`blockstack/blockstack/packaging/pypi-secrets/muneeb`
1. Docker containers are built automatically on Quay.

1. Update `node.blockstack.org` servers
  * [Instructions](https://github.com/blockstackinc/devops/blob/master/blockstack-core/troubleshooting)
1. Update `core.blockstack.org` server
  * [Instructions](https://github.com/blockstackinc/devops/tree/master/core.blockstack.org)
