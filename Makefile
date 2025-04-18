all: vtester

vtester:
	pip install -r requirements.txt
	pyinstaller --onefile vtester.py
	@echo "VTester executable created in dist directory."

clean:
	rm -rf build dist vtester.spec
	@echo "Cleaned up build artifacts."