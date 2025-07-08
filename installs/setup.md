Specify files/folders you want tracked: 

git lfs track "bug_buster_build_env/*"
git lfs track "bug_buster_dev_env/*"
git lfs track "bug_buster1.0/*"
git lfs track "command_tools_globals/*"
git lfs track "installs/*


git add .gitattributes
git commit -m "Track large files with LFS"

git push origin master

wget command - add to environment variables
https://eternallybored.org/misc/wget/



jar for cleaning committed work environments: 
URL: https://rtyley.github.io/bfg-repo-cleaner/

Run this command instead of the one shown in the link where it says 20Mb as opposed to 100mb: 

java -jar command_tool_globals/bfg-1.14.0.jar --strip-blobs-bigger-than 100M some-big-repo.git