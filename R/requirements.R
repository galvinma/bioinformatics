# Requirements install for R 
# Useful when piplining R packages
#
# List of requirements
# Name, Version, Source
#
requirements <- list(
    list("usethis", "2.0.1", "CRAN", "http://cran.us.r-project.org"),
    list("devtools", "2.3.2", "CRAN", "http://cran.us.r-project.org"),
    list("BiocManager", "1.30.12", "CRAN", "http://cran.us.r-project.org"),
    list("ggplot2", "3.3.3", "CRAN", "http://cran.us.r-project.org"),
    list("stringr", "1.4.0", "CRAN", "http://cran.us.r-project.org"),
    list("dplyr", "1.0.5", "CRAN", "http://cran.us.r-project.org"),
)

fetch_bioc_manager <- function(name, version, loc, url, sha)
{
    if (version == "") {
        BiocManager::install(name)
    }
    else {
        BiocManager::install(name, version=version)
    }
}

fetch_cran <- function(name, version, loc, url, sha)
{
    if (version == "") {
        install.packages(name, repos=url)
    }
    else {
        install.packages(name, version=version, repos=url)
    }
}


fetch_requirement <- function(name, version, loc, url, sha)
{
    print(sprintf("Installing %s:%s", name, version))      
    if (loc == 'CRAN'){
        fetch_cran(name, version, loc, url, sha)
    } else if (loc == 'GITHUB') {
        devtools::install_github(url, ref=sha, force = TRUE)
    } else if (loc == 'BIOC_MANAGER') {
        fetch_bioc_manager(name, version, loc, url, sha)
    }
}

for (arr in requirements)
{
    name = arr[[1]]
    version = arr[[2]]
    loc = arr[[3]]
    url = arr[[4]]
    sha = if(loc == "GITHUB") arr[[5]] else ""

    print(sprintf("Checking %s:%s", name, version))
    if (!(name %in% rownames(installed.packages()))) {
        fetch_requirement(name, version, loc, url, sha)
    } else {
        if (version == "") {
            print(sprintf("Using local installation of %s:%s", name, packageVersion(name)))                
        } else if (version == "" | packageVersion(name) != version) {
            print(sprintf("Found incorrect version of requirement %s", name))
            fetch_requirement(name, version, loc, url, sha)
        } else {
            print(sprintf("Found local installation of %s:%s", name, version))
        }
    }

    library(name, character.only = TRUE)
}

