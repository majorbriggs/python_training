set PATH=%PATH%;C:\Program Files (x86)\Git\bin
git checkout gh-pages
rmdir /q /s build _sources _static
git checkout master source Makefile
git reset HEAD
make html
robocopy /move /e build/html ../docs
rmdir /q /s build source Makefile
git add -A
git ci -m "Generated gh-pages"
git push origin gh-pages
git checkout master