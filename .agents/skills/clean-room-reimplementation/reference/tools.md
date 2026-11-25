# Analysis Tool Ladder

## Rung order
- Black-box first, network capture second, tracing third, instrumentation fourth, decompilation last; the order builds the record that only necessary copies were made

## Linux
- Network: mitmproxy, Wireshark, tcpdump
- Trace: strace for syscalls, ltrace for library calls; only one tracer holds ptrace at a time
- Debug: GDB with pwndbg
- Instrument: Frida
- Static: Ghidra, radare2 or Rizin with Cutter, IDA Free for x86 only and non-commercial work

## Windows
- Network: Wireshark, Burp Suite, Fiddler; Proxifier for apps that ignore the system proxy
- Trace: Process Monitor for file, registry, and process events; API Monitor for decoded Win32 calls
- Debug: x64dbg, WinDbg with Time Travel Debugging
- Instrument: Frida
- Static: Ghidra, IDA; dnSpyEx or ILSpy for .NET; Detect It Easy for packer triage

## macOS
- Inspect first: codesign -dv, codesign -d --entitlements :-, otool -L, jtool2
- Debug: LLDB; SIP and the get-task-allow entitlement block attaching to signed release apps
- Trace: dtrace, fs_usage
- Instrument: Frida
- Static: Hopper for Objective-C and Swift, Ghidra, radare2

## Android
- Static: jadx for readable Java, apktool for resources and smali
- Dynamic: objection over Frida for hooking and sslpinning disable, on your own test device only
- Network: Burp or mitmproxy on a test device or emulator you own; try no-CA capture first (plain HTTP, app-level logs). Android 7 and above ignores user-installed CAs, so only on an emulator or test device you own may you push the proxy CA to the system store; never on a daily-use device
- Automated triage: MobSF

## iOS
- Static: Hopper on the IPA, frida-ios-dump on your own jailbroken test device
- Dynamic: Frida gadget injection, objection
- Network: remote virtual interface on a simulator or test device you own; try no-CA capture first (plain HTTP, app-level logs). Only on a simulator or test device you own may you trust a proxy CA in certificate trust settings; never on a daily-use device

## Cross-platform constant
- Frida hooks functions on Linux, Windows, macOS, Android, and iOS; it is the highest-leverage single tool in this workflow