# Travel Booking Application

project link : https://midhun.pythonanywhere.com/


A Django-based travel booking application that allows users to browse and search for travel options including flights, trains, and buses.

 Project Structure


travel_application/
├── travel_booking/          # Main project settings
├── booking/                 # Main app
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── urls.py             # URL routing
│   ├── forms.py            # Form classes
│   └── admin.py            # Admin interface
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   ├── home.html           # Home page
│   ├── login.html          # Login page
│   ├── register.html       # Registration page
│   └── profile.html        # Profile page
└── manage.py               # Django management script
```

## Setup Instructions

### 1. Install Dependencies

# Create virtual environment 
python -m venv venv
venv\Scripts\activate  # On Windows


# Install Django
pip install django
```

### 2. Database Setup
```bash

python manage.py migrate


python manage.py createsuperuser
```

### 3. Run the Application
```bash
python manage.py runserver
```

The application will be available at:
- Home Page: http://localhost:8000/
- Admin Panel: http://localhost:8000/admin/
- Login: http://localhost:8000/login
- Register: http://localhost:8000/register/

## Default Admin Credentials
- **Username**: admin
- **Password**: admin123

## Sample Data

The application comes with sample travel options including:
- Flights: Mumbai-Delhi, Delhi-Bangalore
- Trains: Mumbai-Pune, Delhi-Agra
- Buses: Mumbai-Nashik, Pune-Mumbai

## Features Implemented

✅ **User Authentication System**
- User registration with email
- Login/logout functionality
- Profile update capability
- Password change support

✅ **Travel Options Display**
- List all available travel options
- Filter by type (Flight/Train/Bus)
- Search by source and destination
- Responsive card-based layout


✅ **Admin Interface**
- Travel options management
- User management
- Booking management

✅ **Responsive UI**
- Bootstrap 5 styling
- Mobile-friendly design
- Clean and modern interface


### 1. **Booking Creation System**
- Users can select travel options and book seats
- Real-time price calculation based on number of seats
- Seat availability validation
- Automatic seat deduction from available inventory
- Transaction safety with database atomic operations

### 2. **Booking Management**
- View all current and past bookings
- Cancel confirmed bookings
- Automatic seat restoration when bookings are cancelled
- Booking status tracking (Confirmed/Cancelled)

### 3. **Enhanced User Interface**
- "Book Now" buttons on travel options (only for authenticated users)
- Dynamic seat availability display
- Responsive booking forms with real-time price updates
- Clear booking confirmation and cancellation interfaces




## 📱 User Experience Flow

### **Making a Booking:**
1. User browses travel options on home page
2. Clicks "Book Now" button on desired travel option
3. Fills in number of seats required
4. Views real-time total price calculation
5. Confirms booking
6. Receives confirmation with booking ID
7. Redirected to "My Bookings" page

### **Managing Bookings:**
1. User navigates to "My Bookings" from navigation
2. Views all current and past bookings
3. Can cancel confirmed bookings
4. Sees booking status, details, and total price
5. Easy navigation back to browse more options

### **Cancelling Bookings:**
1. User clicks "Cancel Booking" on confirmed booking
2. Views cancellation confirmation page
3. Confirms cancellation
4. Seats are automatically restored to inventory
5. Booking status updated to "Cancelled"


### **Smart Seat Management:**
- Real-time seat availability checking
- Automatic seat deduction on booking
- Seat restoration on cancellation
- Prevents over-booking

### **Price Calculation:**
- Real-time total price updates
- Based on number of seats selected
- Clear price per seat display

### **Security Features:**
- Login required for all booking operations
- Users can only manage their own bookings
- Database transactions ensure data consistency

### **User Interface:**
- Bootstrap-styled responsive design
- Clear visual indicators for booking status
- Intuitive navigation between pages
- Helpful error messages and confirmations

## 🚀 How to Use

### **For Users:**
1. **Login/Register** to access booking features
2. **Browse** travel options on the home page
3. **Click "Book Now"** on desired travel option
4. **Enter number of seats** and confirm booking
5. **View bookings** in "My Bookings" section
6. **Cancel bookings** if needed (confirmed bookings only)

### **For Administrators:**
1. **Access admin panel** at `/admin/`
2. **Manage travel options** - add, edit, remove
3. **View all bookings** across all users
4. **Monitor seat availability** and booking statuses

## 🔍 Testing the Features

### **Test Scenarios:**
1. **Create a booking** - Select travel option, enter seats, confirm
2. **View bookings** - Navigate to "My Bookings" page
3. **Cancel booking** - Cancel a confirmed booking
4. **Seat validation** - Try to book more seats than available
5. **Authentication** - Ensure only logged-in users can book



## URL Structure

- `/` - Home page with travel options
- `/login/` - User login
- `/register/` - User registration
- `/profile/` - User profile management
- `/logout/` - User logout
- `/admin/` - Admin interface

## Models

### TravelOption
- Type (Flight/Train/Bus)
- Source and destination
- Date and time
- Price and available seats

### Booking
- User reference
- Travel option reference
- Number of seats and total price
- Booking status and date

### User
- Extended Django User model
- Profile information (first name, last name, email)

## Technologies Used

- **Backend**: Django 5.2.5
- **Database**: SQLite (development)
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Authentication**: Django built-in auth system
- **Forms**: Django forms with Bootstrap styling


