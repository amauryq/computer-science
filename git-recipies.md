# Git Recipies

## Update loca list of remote branch

```bash
git remote update origin --prune
```

## Download a full GitHub Organization

```bash
curl "https://github.com/api/v3/orgs/ORGANIZATION/repos?per_page=200&access_token=<access-token>" |   grep -e 'ssh_url*' |   cut -d \" -f 4 |   xargs -L1 git clone
```

## Mirroring a repository

### Create a bare clone of the repository

```bash
$ git clone --bare https://github.com/exampleuser/old-repository.git
```

### Mirror-push to the new repository

```bash
$ cd old-repository.git
$ git push --mirror https://github.com/exampleuser/new-repository.git
```

### Remove the temporary local repository you created in step 1

```bash
$ cd ..
$ rm -rf old-repository.git
```
