package com.example.devices;

import com.example.devices.exception.ResourceNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/devices")
public class DeviceController {

    @Autowired
    private DeviceRepository deviceRepository;

    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }

    @Autowired
    private RestTemplate restTemplate;

    @PostMapping
    public Device createDevice(@RequestBody Device device) {
        return deviceRepository.save(device);
    }

    @GetMapping
    public List<Device> getAllDevices() {
        return deviceRepository.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Device> getDeviceById(@PathVariable Long id) {
        Device device = deviceRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException ("Device not found"));
        return ResponseEntity.ok(device);
    }

    @PostMapping("/predict/{deviceId}")
    public ResponseEntity<Device> predictDevicePrice(@PathVariable Long deviceId) {
        Device device = deviceRepository.findById(deviceId)
                .orElseThrow(() -> new ResourceNotFoundException("Device not found"));

        int predictedPrice = predictPrice(device);
        device.setPriceRange(predictedPrice);

        return ResponseEntity.ok(deviceRepository.save(device));
    }

    private int predictPrice(Device device) {
        HttpEntity<Device> request = new HttpEntity<>(device);
        ResponseEntity<Map> response = restTemplate.exchange(
                "http://localhost:5000/predict", HttpMethod.POST, request, Map.class);
        Map<String, Integer> responseBody = response.getBody();
        return responseBody.get("price_range");
    }
}
