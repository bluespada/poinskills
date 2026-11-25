# Tool Ladder

## Reading order
- Start outside the binary and move inward: run it, capture its traffic,
  trace it, instrument it, open it last. Each step must earn its place, so
  the record shows only necessary copies were made.

## Linux
- Traffic: mitmproxy, Wireshark, tcpdump.
- Trace: strace for syscalls, ltrace for library calls. One tracer holds ptrace at a time.
- Debug: GDB with pwndbg.
- Instrument: Frida.
- Open: Ghidra, radare2 or Rizin with Cutter, IDA Free for x86 only and non-commercial work.

## Windows
- Traffic: Wireshark, Burp Suite, Fiddler. Proxifier covers apps that ignore the system proxy.
- Trace: Process Monitor for file, registry, and process events. API Monitor for decoded Win32 calls.
- Debug: x64dbg, WinDbg with Time Travel Debugging.
- Instrument: Frida.
- Open: Ghidra, IDA, dnSpyEx or ILSpy for .NET, Detect It Easy for packer triage.

## macOS
- Look first: codesign -dv, codesign -d --entitlements :-, otool -L, jtool2.
- Debug: LLDB. SIP and the get-task-allow entitlement block attaching to signed release apps.
- Trace: dtrace, fs_usage.
- Instrument: Frida.
- Open: Hopper for Objective-C and Swift, Ghidra, radare2.

## Android
- Open: jadx for readable Java, apktool for resources and smali.
- Instrument: objection over Frida for hooking and pinning workarounds, on your own test device only.
- Traffic: Burp or mitmproxy on a test device or emulator you own. Try capture
  without a custom CA first (plain HTTP, app-level logs). Android 7 and up
  ignores user-installed CAs, so only on an emulator or test device you own
  may you push the proxy CA into the system store. Never on a daily-use device.
- Triage: MobSF for a first automated pass.

## iOS
- Open: Hopper on the IPA, frida-ios-dump on your own jailbroken test device.
- Instrument: Frida gadget injection, objection.
- Traffic: remote virtual interface on a simulator or test device you own.
  Try capture without a custom CA first. Only on a simulator or test device
  you own may you trust a proxy CA in certificate settings. Never on a
  daily-use device.

## Constant across platforms
- Frida hooks functions on Linux, Windows, macOS, Android, and iOS. It is
  the highest-leverage single tool in this runbook.
