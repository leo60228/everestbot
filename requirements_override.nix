{ pkgs, python }:

self: super: {
    "asyncio" = python.overrideDerivation super."asyncio" (old: {
        buildInputs = old.buildInputs ++ [ self."setuptools-scm" ];
    });
    "python-dateutil" = python.overrideDerivation super."python-dateutil" (old: {
        buildInputs = old.buildInputs ++ [ self."setuptools-scm" ];
    });
    "discord.py" = python.overrideDerivation super."discord.py" (old: {
        src = pkgs.fetchgit {
            url = "https://github.com/Rapptz/discord.py";
            sha256 = "1qlcv0h5m2jdvqk9kayiacl2i5cbdjgv9dbgfa3cy26wrdgmkss2";
            rev = "dec14faea90b57d34245b17e58438ee91990764c";
        };
    });
}
