# Smallify-comics

## Requirements
smallifiy uses Image Magick, please install first
`sudo apt-get install imagemagick`

## Install
Put files into a known folder of your PATH (exemple : `.local/bin`)
or make links (ln) between your git clone folder files, and your path `.local/bin`

Make sure they have execution (x) permission

(if not, `chmod +x filename`)

## Use
In a folder containing multiple cbr and/or cbz files,

open a Terminal and type :

`smallify-all`

For recursive, you can use :

`smallify-recurse.py`
(all sub-folders)

`smallify-recurse.py -d 2`
(2 sub-level depth)

for current folder only
`smallify-recurse.py -d 0`

## License
[GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0)
