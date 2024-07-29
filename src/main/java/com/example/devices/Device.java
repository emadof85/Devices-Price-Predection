package com.example.devices;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
@Entity
public class Device {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	private int batteryPower;
	private int blue;
	private float clockSpeed;
	private int dualSim;
	private int fc;
	private int fourG;
	private int intMemory;
	private float mDep;
	private int mobileWt;
	private int nCores;
	private int pc;
	private int pxHeight;
	private int pxWidth;
	private int ram;
	private int scH;
	private int scW;
	private int talkTime;
	private int threeG;
	private int touchScreen;
	private int wifi;
	private int priceRange;

	// Getters and setters

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public int getBatteryPower() {
		return batteryPower;
	}

	public void setBatteryPower(int batteryPower) {
		this.batteryPower = batteryPower;
	}

	// Other getters and setters ...

	public int getPriceRange() {
		return priceRange;
	}

	public void setPriceRange(int priceRange) {
		this.priceRange = priceRange;
	}
}