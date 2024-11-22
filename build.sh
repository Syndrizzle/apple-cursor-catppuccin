#!/bin/bash
# A script for preparing binaries of Apple Cursors, created by Abdulkaiz Khatri.

version="v2.0.1"

error() (
  set -o pipefail
  "$@" 2> >(sed $'s,.*,\e[31m&\e[m,' >&2)
)

get_config_file() {
  local key="${1}"
  local cfg_file="build.toml"

  if [[ $key == *"Right"* ]]; then
    cfg_file="build.right.toml"
  fi

  echo $cfg_file
}

with_version() {
  local comment="${1}"
  echo "$comment ($version)"
}

if ! type -p ctgen >/dev/null; then
  error ctgen
  exit 127 # exit program with "command not found" error code
fi

declare -A names
names["macOS-Catppuccin-Latte-Dark"]=$(with_version "Catppuccin Latte Dark")
names["macOS-Catppuccin-Latte"]=$(with_version "Catppuccin Latte")
names["macOS-Catppuccin-Frappe-Dark"]=$(with_version "Catppuccin Frappe Dark")
names["macOS-Catppuccin-Frappe"]=$(with_version "Catppuccin Frappe")
names["macOS-Catppuccin-Macchiato-Dark"]=$(with_version "Catppuccin Macchiato Dark")
names["macOS-Catppuccin-Macchiato"]=$(with_version "Catppuccin Macchiato")
names["macOS-Catppuccin-Mocha-Dark"]=$(with_version "Catppuccin Mocha Dark")
names["macOS-Catppuccin-Mocha"]=$(with_version "Catppuccin Mocha")

# Cleanup old builds
rm -rf themes bin

# Building Apple XCursor binaries
for key in "${!names[@]}"; do
  comment="${names[$key]}"
  cfg=$(get_config_file key)

  ctgen "configs/x.$cfg" -p x11 -d "bitmaps/$key" -n "$key" -c "$comment XCursors" &
  PID=$!
  wait $PID
done

# Building macOS Windows binaries
for key in "${!names[@]}"; do
  comment="${names[$key]}"
  cfg=$(get_config_file key)

  ctgen "configs/win_rg.$cfg" -d "bitmaps/$key" -n "$key-Regular" -c "$comment Regular Windows Cursors" &
  ctgen "configs/win_lg.$cfg" -d "bitmaps/$key" -n "$key-Large" -c "$comment Large Windows Cursors" &
  ctgen "configs/win_xl.$cfg" -d "bitmaps/$key" -n "$key-Extra-Large" -c "$comment Extra Large Windows Cursors" &
  PID=$!
  wait $PID
done

python3 fix_inf.py

# Compressing Binaries
mkdir -p bin
cd themes || exit

for key in "${!names[@]}"; do
  tar -cJvf "../bin/${key}.tar.xz" "${key}" &
  PID=$!
  wait $PID
done

# Compressing macOS-*-Windows
for key in "${!names[@]}"; do
  zip -rv "../bin/${key}-Windows.zip" "${key}-Regular-Windows" "${key}-Large-Windows" "${key}-Extra-Large-Windows" &
  PID=$!
  wait $PID
done

cd ..
