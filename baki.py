from internetarchive import download

main_folder = "animeancestors_bakithegrappler_300722/"
download(
    main_folder,
    glob_pattern="*.mkv",
    verbose=True,
    destdir="./tv shows/Baki the grabbler/",
    ignore_existing=True,
)
