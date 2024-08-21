package com.example.gpsapp;

import android.Manifest;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.BatteryManager;
import android.os.Bundle;
import android.widget.Toast;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

public class MainActivity extends AppCompatActivity {

    private LocationManager locationManager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        locationManager = (LocationManager) getSystemService(LOCATION_SERVICE);

        checkPermissionsAndRequestLocation();
    }

    private void checkPermissionsAndRequestLocation() {
        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED &&
            ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.ACCESS_FINE_LOCATION}, 1);
            return;
        }

        manageBatteryAndLocationUpdates();
    }

    private void manageBatteryAndLocationUpdates() {
        BatteryManager batteryManager = (BatteryManager) getSystemService(BATTERY_SERVICE);
        int batteryLevel = batteryManager.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY);

        if (batteryLevel < 20) {
            // 低电量模式
            locationManager.requestLocationUpdates(LocationManager.NETWORK_PROVIDER, 0, 0, locationListener);
        } else {
            // 高精度GPS模式
            locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, locationListener);
        }
    }

    private LocationListener locationListener = new LocationListener() {
        @Override
        public void onLocationChanged(@NonNull Location location) {
            try {
                double latitude = location.getLatitude();
                double longitude = location.getLongitude();

                sendLocationToPython(latitude, longitude);
            } catch (Exception e) {
                e.printStackTrace();
                runOnUiThread(() -> Toast.makeText(MainActivity.this, "无法获取位置", Toast.LENGTH_LONG).show());
            }
        }

        @Override
        public void onProviderDisabled(@NonNull String provider) {
            runOnUiThread(() -> Toast.makeText(MainActivity.this, "GPS未启用，请检查设置", Toast.LENGTH_LONG).show());
        }
    };

    private void sendLocationToPython(double latitude, double longitude) {
        // 通过JNI或Pyjnius将位置数据发送到Python代码
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        if (requestCode == 1) {
            if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                // 权限被授予，继续获取位置
                manageBatteryAndLocationUpdates();
            } else {
                runOnUiThread(() -> Toast.makeText(this, "权限被拒绝，无法获取位置", Toast.LENGTH_LONG).show());
            }
        }
    }
}
