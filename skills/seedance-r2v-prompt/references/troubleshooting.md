# Seedance diagnosis
| Symptom | Inspect | Repair |
|---|---|---|
| New clip generated instead of editing source | “Reference Video” phrasing misclassifies task | Directly say edit/extend the actual Video source |
| Async task mismatch | Prompt intent conflicts with 2.5 task flag | Align reference/edit/extend intent and supported parameter combination |
| Source edit rejects ratio/duration | Non-adaptive ratio or fixed seconds on 2.5 edit | Use adaptive and -1 as required |
| Faces drift/duplicate | Tiny face in a collage, unbound multiple views | Assign one identity explicitly and improve the actual source if authorized |
| Donor performer replaces target | Motion and appearance roles mixed | Borrow only the action/camera dimension |
| Unwanted subtitles | Source type or speech formatting triggers captions | Omit subtitle markers, specify clean screen; inspect output |
| Voice does not match | Timbre source includes music/unclear role | Assign clean actual voice reference and new dialogue clearly |
| Speech in wrong language | Language not stated or text translated | Keep exact line and label Korean/other language explicitly |
| Camera drifts | Source-camera role or conflicting tracking language | Separate actor motion and explicit fixed target camera |
| Extension jumps | Source end state not carried forward | Continue pose, motion, camera and sound at the seam |
| Style becomes realistic | Motion donor's medium leaked | State the target medium consistently, exclude donor appearance/style role |
| Ending noise/artifacts | Too much action/dialogue for runtime | Simplify timeline or use a longer supported duration |
| Effect looks generic | Effect origin and physical interaction absent | Describe onset, geometry, movement and environmental consequence |
| Parameter accepted by one provider but refused by another | Shared schema mistaken for universal capability | Use actual model/version/provider profile and report the conflict |

Record asset order/roles, total duration, output framing, audio flag and task type with the prompt. Inspect identity, choreography, source preservation, speech, subtitles, seam and actual length independently. A valid text specification cannot certify a generated result without viewing it.
