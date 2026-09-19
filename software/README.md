# 💻 CattleΨic Software

The CattleΨic software layer connects the Raspberry Pi edge device with farmer-facing outputs and the backend/dashboard architecture.

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

### Farmer Dashboard

The dashboard is designed to display:

- Cow-wise health records
- Latest milk-test readings
- Mastitis risk status
- Historical test results
- Device information
- Alert information

### Backend

The backend handles / is planned to handle:

- Device data reception
- Health-record storage
- Dashboard APIs
- Cow-wise test history
- Cloud synchronization

### Thermal Receipt Output

A receipt formatter scaffold is available under:

`hardware/thermal-printer/receipt_formatter.py`

The printed receipt design includes Cow ID, date/time, sensor readings and screening risk status. Physical printer communication will be added after the exact 58 mm printer model is finalized.

## Current Status

✅ Dashboard prototype developed  
✅ Backend API prototype developed  
✅ Device-data simulation available  
✅ Receipt formatter scaffold available  

🟡 Raspberry Pi live synchronization in progress  
🟡 Physical thermal-printer integration pending  
🟡 Production deployment pending  
🟡 ML integration and validation in progress
