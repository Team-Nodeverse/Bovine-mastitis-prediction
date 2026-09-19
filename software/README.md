# 💻 CattleΨic Software

The CattleΨic software layer connects the Raspberry Pi edge device with the trained Random Forest risk model, large local display, farmer dashboard, offline storage, cloud/backend path and thermal receipt output.

## Software Modules

### Raspberry Pi Edge Layer

The Raspberry Pi prepares one structured test result containing:

- Cow ID
- test timestamp
- pH
- electrical conductivity
- temperature
- turbidity
- risk status

The same result object is intended to feed every output so values remain consistent.

### AI / ML Layer

- Random Forest model training is completed on the currently available labelled dataset.
- Final Raspberry Pi model-artifact integration and deployment validation are being completed.
- Evaluation metrics should be published from the actual model run only.

### Large Local Display

The earlier 16x4 character LCD concept has been removed from the current hardware direction.

The large display / touchscreen UI is designed to show:

- Cow ID
- live sensor values
- test progress
- risk level
- next-step guidance
- connectivity state
- print status

Display module: `hardware/display/`

### Farmer Dashboard

The dashboard is designed to display:

- Cow-wise health records
- Latest milk-test readings
- Mastitis risk status
- Historical test results
- Device information
- Alert information

### Backend / Cloud

The backend architecture handles / is intended to handle:

- Device data reception
- Health-record storage
- Dashboard APIs
- Cow-wise test history
- Cloud synchronization
- alert routing

### Thermal Receipt Output

A receipt formatter scaffold is available under:

`hardware/thermal-printer/receipt_formatter.py`

The 58 mm printed receipt is part of the current device architecture and can contain Cow ID, date/time, sensor readings and risk status.

## Current Status

✅ Dashboard prototype developed  
✅ Backend API prototype developed  
✅ Device-data simulation available  
✅ Random Forest model trained  
✅ Large-display software interface available  
✅ Receipt formatter scaffold available  

🟡 Raspberry Pi model deployment integration  
🟡 Raspberry Pi live synchronization  
🟡 Physical thermal-printer integration  
🟡 Final display mounting / enclosure integration  
🟡 Production / field validation

## Repository Note

The full production dashboard/backend source should be added under `software/` when the final source package is ready for public submission. Do not upload `.env` files, API secrets, service-role keys or real user data.
