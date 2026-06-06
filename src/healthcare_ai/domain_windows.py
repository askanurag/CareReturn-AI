from .domain_contract import validate_recording
def segments(frame,seconds=30,stride=1):
    # Discharge snapshots are single-row index encounters, not signal windows.
    validate_recording(frame)
    if seconds<1 or stride<1:raise ValueError('Positive horizon and stride required')
    return [frame.iloc[[i]].copy() for i in range(0,len(frame),int(stride))]
