---
name: broker-and-infrastructure-reliability
description: 'Use this skill when deploying a strategy to run live or paper, to build the infrastructure-level reliability (reconnect logic, outage handling, redundancy, silent-failure detection) that keeps it actually running and known-to-be-running. Also use it when a user asks "what if my broker connection drops" or "how do I know if my algo is still trading." This skill exists because a live trading system''s biggest infrastructure risk often isn''t a wrong decision, it''s the system silently stopping without anyone knowing, whether from an API outage, an unhandled exception, or a network interruption, while positions sit unmanaged in the meantime.'
---

# Broker and Infrastructure Reliability

## Why this matters

A strategy that's statistically sound, well-sized, and passed forward testing can still cause real damage if the infrastructure running it fails silently: a dropped connection that goes unnoticed, an unhandled exception that kills the process without alerting anyone, or a broker outage that leaves an open position unmanaged during exactly the kind of volatile conditions when management matters most. This isn't a strategy-design problem, it's an operational reliability problem, and it needs its own explicit attention rather than being assumed to be handled by whatever framework or library the strategy happens to be built on.

## Do this

### Build explicit reconnect logic for every network/API dependency, and test it by actually triggering a disconnect

A live trading system depends on a broker API connection, a market data feed connection, and often other network services, and any of them can drop unexpectedly. Build explicit reconnect logic (with backoff, and a check that reconnection actually restores correct state rather than assuming a fresh connection is automatically consistent with what happened during the outage) for each dependency, and actually test it by deliberately triggering a disconnect in a safe environment, rather than assuming a library's default reconnect behavior is adequate without having verified it.

### Detect and alert on silent process failure, not just on errors the process itself reports

An unhandled exception, an out-of-memory condition, or a host-level failure can stop a trading process entirely without it ever getting the chance to log or report an error about itself. Build monitoring external to the trading process itself, a separate heartbeat or watchdog check, that alerts specifically when the process has stopped running or stopped producing expected activity, since a process that's already dead can't be relied on to report its own death.

### Explicitly define what happens to open positions during a broker outage or connectivity loss

An open position doesn't pause just because the connection managing it drops; decide in advance what should happen to open positions during an outage (do existing stop-loss orders remain active on the broker's side even without the strategy's process connected, is there a fallback mechanism, is there a maximum acceptable outage duration before a different action is required) rather than discovering the answer only when an actual outage occurs while a position is open.

### Build redundancy appropriate to the strategy's actual risk profile, not none and not more than needed

A slow, infrequently-trading strategy with modest position sizes may reasonably tolerate a brief connectivity gap with minimal real risk; a fast strategy or one carrying meaningful leveraged exposure may need real redundancy (a backup connection path, a secondary monitoring system, a broker-side stop order as a backstop independent of the strategy's own process). Match the actual investment in redundancy to the strategy's real risk profile and trading frequency, rather than either skipping redundancy entirely or over-building it for a strategy that doesn't need it.

### Log everything needed to reconstruct what the system believed and did, for after-the-fact review

When something does go wrong, being able to reconstruct exactly what the system's state and decisions were leading up to the failure is essential for actually fixing the root cause rather than guessing at it. Log strategy decisions, order requests, fills, connection state changes, and errors with enough detail and enough retention to reconstruct a timeline after the fact, not just enough to see that something went wrong.

## Never do this

- Never assume a library's or framework's default reconnect behavior is adequate without having actually tested it by triggering a real disconnect.
- Never rely solely on the trading process's own error reporting to detect that something has gone wrong; build external, independent monitoring that can detect the process has stopped entirely.
- Never leave the behavior of open positions during a broker outage undefined until an actual outage happens while positions are open.
- Never build redundancy investment disconnected from the strategy's actual risk profile and trading frequency, either skipping it entirely for a fast/leveraged strategy or over-engineering it for a strategy that doesn't need it.
- Never log only enough to notice that a failure occurred; log enough detail and retain it long enough to reconstruct what the system believed and did leading up to it.

## Verification checklist

- [ ] Reconnect logic exists for every network/API dependency and has actually been tested by triggering a real disconnect, not assumed adequate
- [ ] External, independent monitoring (a heartbeat/watchdog) exists that can detect the trading process has stopped entirely, not only monitoring that depends on the process reporting its own errors
- [ ] The behavior of open positions during a broker outage or connectivity loss is explicitly defined and tested, not left to be discovered during an actual outage
- [ ] Redundancy investment (backup connections, broker-side backstop orders, secondary monitoring) is matched to the strategy's actual risk profile and trading frequency
- [ ] Logging captures enough detail, with enough retention, to reconstruct the system's state and decisions leading up to any failure after the fact
