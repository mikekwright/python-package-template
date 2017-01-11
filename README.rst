{{APP_NAME}}
=============================

Place the description of your library in here

## Use Template

To use the template you will want to pull down this repo as the starting point, then
you will need to point the remote at the new repo location.  

    git remote set-url origin <new_url>

After setting the origin remote you will need to run the configure command that will
replace all the {{APP_NAME}}, {{DESC}} and {{URL}} entries in specified files.   

    bin/template/configure

Now go ahead and commit the built package to your new repo    

    git add .
    git commit -m "Created a new python package"
    git push origin master


