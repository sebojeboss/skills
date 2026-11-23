# Cart identity and state

## When to read

Wrong variant or row; the second edit fails; a duplicate line; a stale drawer; removing one discount removes others.

## How to do the work

Ask two questions separately: **which row**, and **which version of the cart**.

**Which row.** Read the product selector's actual submitted value, not its visible label. Changing a label without binding the selected value into the submitted form still adds the default variant. Confirm the selected variant exists and carries the intended price and availability. Then check whether two rows share a variant while differing in personalization, selling plan or other line properties. A plain unit and a personalized unit of the same variant are two lines, and a quantity control keyed on variant ID will hit the wrong one. Target the row by the platform's current line identity, never by product title or a cached array position. Preserve property types: a string "true" and a boolean true can make otherwise identical lines diverge.

**Which version.** Record the cart revision before the mutation and the returned lines afterward. Line identifiers can change when a discount threshold, quantity or property changes a line's characteristics. Take the next command's identity from that result.

Illustrative: an automatic discount starts at a quantity threshold. The edit that crosses the threshold succeeds; the next edit fails because the page still holds the old key. Compare the request payload, the response and the rendered key: that distinguishes a stale identity from a failed first mutation.

A positional API still needs the current ordering, and positions shift after an earlier row is removed. When concurrent edits are possible, choose serialization or revision-aware reconciliation to suit the existing architecture. Disabling every control indefinitely sacrifices usability without repairing stale state.

**Stale drawer.** Split the operation into three steps: suppress native navigation, perform the mutation, then show its result. If the mutation succeeded and only the section markup failed, recover the rendering. Repeating the add because the drawer stayed unchanged can duplicate merchandise. Find the actual owner of the fetched markup and the event listeners. Check whether a listener still targets a removed node. Give rendering one owner that every initiating control shares, rather than competing renderers per button. A drawer can show items before its quantity controls, removal and header count are wired; each intermediate success proves less than the finished interaction. After the repair, retest remove, quantity change and an unrelated row.

**Discount removal.** A per-code remove button can look individual while sending "no discount", which clears every code. Apply two codes, remove one, and confirm the other survives in the returned cart, not just in the drawer.
