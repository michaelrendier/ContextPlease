"""Ainur.load_context()/save_context() on a TEMP COPY of claude_context.json: truncate the file (crash mid-write), load, save.
Run from PtolemyDesktop/. The repo file is never touched."""
import sys, types, shutil, tempfile, json, os, importlib.util
sys.path.insert(0, os.getcwd()); sys.modules.setdefault("anthropic", types.ModuleType("anthropic"))
spec = importlib.util.spec_from_file_location("ainur", "Philadelphos/Ainur/ainur.py"); ainur = importlib.util.module_from_spec(spec); spec.loader.exec_module(ainur)
tmp = tempfile.mkdtemp(); f = os.path.join(tmp, "claude_context.json"); shutil.copy("Philadelphos/context/claude_context.json", f); ainur._CONTEXT_FILE = f
obj = object.__new__(ainur.Ainur); print("before:", list(json.load(open(f))), os.path.getsize(f), "bytes")
open(f, "w").write(open(f).read()[:1500]); print("load_context() after truncation ->", obj.load_context())
obj.save_context(); a = json.load(open(f)); print("after one save_context():", list(a), os.path.getsize(f), "bytes")
