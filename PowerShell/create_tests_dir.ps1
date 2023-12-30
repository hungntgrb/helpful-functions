param(
    [string]$rootdir=".\"
)

New-Item -Path "$($rootdir)tests\__init__.py" -Force;
New-Item -Path "$($rootdir)tests\unit\__init__.py" -Force;
New-Item -Path "$($rootdir)tests\integration\__init__.py" -Force;
New-Item -Path "$($rootdir)tests\system\__init__.py" -Force;
