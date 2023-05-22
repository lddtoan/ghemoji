python -m nuitka --follow-imports --standalone --onefile --remove-output ./ghemoji/main.py
mkdir -p dist
mv main.bin ./dist/ghemoji