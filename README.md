# 🔌 Port Status Monitoring Tool (SDN)

## 📌 Overview

This project implements a **Software Defined Networking (SDN)** application that monitors switch port status in real time using the **Ryu Controller** and **Mininet**.

The system detects and logs **port state transitions (UP/DOWN)** dynamically by listening to OpenFlow events. This provides visibility into network behavior and helps in identifying link failures or topology changes.

---

## 🎯 Objectives

* Monitor switch port status changes (UP/DOWN)
* Capture OpenFlow port events from switches
* Log real-time network changes
* Simulate SDN architecture using Mininet
* Understand controller-based network management

---

## 🧠 Technologies Used

* **Mininet** – Network emulation platform
* **Ryu Controller** – SDN controller framework
* **OpenFlow 1.3** – Southbound protocol
* **Python** – Implementation language

---

## 🏗️ System Architecture

![Image](https://images.openai.com/static-rsc-4/AxC1nAt-AoLCMr4FYmCOHYI7PJp6z5rnmPv021VnOnCac_0aqnevUe-8rjCRmruNZdEFl2bjpE4RgSxDepmPkqp80ZjOcWAUNWKWNVt4d0FI6vCDsDWFwaL0ba-k2tfN1732-ZdYGo_qf5nnuBPKvpQNJ2OrI6doRXFVqR7EY8lffbMzFWF3eN3JGWM9VOtB?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/tJrNnjHRmOqDpaoF2q5hRo_-Gb7Xb4QNqi2mSXIlv7Lvdb3M6OkSzK5Bp9vgOoaTrX6t_0K6q1ulwToOn8ZUPuz05AYX1HOn3bL7qxp2dbH8gYzku7KHixBtfOOQ3ibugzCyBk3lg-3rEsknTCpIeBLx2QQnE6qcimkWfZi9erK2scH2xYUAmjqUQucMjrJO?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/jpxOnayr3JUXprWFZWIK2S9S2tw_v2gR_hNyEFP4JtXvnUD-1vfYcB7gMgRuDB7-G0T3M8ClwvAmJKtETmb5fbg4oqtKQpWren3KUGBkY9oIAkJTtpNIdNlysSugPrQLnl35zralkXDo7bCvNmsc1oGVsvBUfs-OEK3sGCYa2TaaOyCf74ngTQG59pqQS8gY?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/UeYMxhVErDiEOQBuz5-MpV3W2v6_WaOrkkbVR1JNqseUTRBBZKNDNGv1etodDqLhLPCsVxfKLymHrCr_oeTcotcGhDZeWQzA7_0OcDzGh_oHuEVnKEceq1gucrjsHEiEfa0rOe_RKjbuFiFnfD2C6JPAmRKzWiUV2Ayr2u8HsRjPtS3z6h5GCpahFepU3JJN?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/L-4YwMiNShmNca_zRC8YRRuVqisBcoTd7lT4kL96veNcl_N5zFfbJ2Hw4F6lY44KTMuhZh3KVBW4RZpOQbX9IUcpZaosyt8tSaUD77N3IVfqCKK-GxHzYtJiHrdAyMbaHoQ5B5zG38dM7yzegW9GT_WRo52GpX_vdghm5f31JUBQgNOuW9BsI7MadvwCe48B?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/-O1Pz3jTP7v51yQEgaagj7dw2R4hmkqDIumNM68Z1Por0u1r7NXcuVRxskVd2d3h9xAu9nnrdL6kALFgfEc40mZZs3k4bYBySIzIceVyh4QtP2xrdBwSOa9FiyE3-4LZc2rHLnxKVMT3pIKJzAN6dsWbAn0RQVLq_ZypsEVhbok0W7Q2XrHyJY0K9TQSg11h?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/SEDmahtUc58FUjspfEOQ8sRVzNLtmoJLWjMC3pvPfzMJLajytEKBSNN2y6EJKdY9NWa0xUDolbimr8KKouW-RsWY_gy5iYjEn-bglXw4QJTRh_G7hGQJYACGcqtlktJoymX2xUsT0npaRtTTA0mIUMLw1AGXqbsCxOyrrmKP9fFhVns1V0jwj63YD7CgrYSb?purpose=fullsize)

### Explanation:

* Hosts are connected to a switch in Mininet
* The switch is managed by the Ryu controller
* Communication happens using the OpenFlow protocol
* The controller listens for port status updates from switches

---

## ⚙️ Working Principle

![Image](https://images.openai.com/static-rsc-4/qze1oBtvzE6jQs--07hZecKlhHTA3SujPeTSjJvdxohuUGGoOIW6Y-NfKcC519rTdbPnPlzmzfwDj1aTpyBAYzwvUkj9ANx2gEpXFg8X6BFainJR3une4PspPYrLgTjolsa8EH6WB0wcNN99YrMM060rSH8U8Ik6ZcskewV-4hqCimbLfLlI9znb6S7604Lk?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/EnenJWRj8oG6DQQ-694m-Ig57lfzxPC-20TmY1etm9kBEyg2KuJ3W2nHXugmMUydNcTVnZBKXScCN_reQhOHCyC2JhsvCnXbIaWBMNASpZMH9_7PML1jPDkhMt4QT7YemoPeK5aHYvWfpo3tIdXCkPmWUFp7F4zAVzgRtVrMF-SmajcaMfmS3Iw--QnwWBq3?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/MGQXX8tjyKeCezU2P-hCBjVH4yF1pZAqTOaXDCGGIc-fPGKOhxePzsdkloYKLZOBomPMipeIeJei8bC08xydtKE-Hk0w2bHhJ3VXUwGIowmevDkx_KsQEQx1TcdtJ6ysSwkfcsU5_PgboZS0vI_Iwix0bCmrFaNddwQ91olhnArcaziqduZZdCrOvFwFfZGs?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/6Dp_blfGgR4k7NROqTgR9T0brGAz-kvVo1TRJB4hiCYrusmMfxclXXN92cBkAFnWgezaflSDr3jOfT9VqXIEQvrxblMjRRIMFfzugrA76KR-g_iUIBfPQfAkn7IxkaXtPGoV-lb78In7y1f1ECoSotKPShK0MDY-VYDUcXnhCIZWjG-pafLEJCmOel9opF1x?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/JTj6Ue893KS0xVmeDFsFwOLGQL5pUd0GQzPrXAfM-_I9dGGUrw3V0F_KcZ5LYZy7XSsXAducRJ_mXD_5e-6KVaOClZmf6gx6W_Ev2T3VjEGbwbIdXztwe-Tyu1U7i3jNlUQSu6KlPUpnituFJqDhz_Cn35JO03cOzx3KdZJaBnnZRA6rb89NRXYRVJe-aEg2?purpose=fullsize)

1. Mininet creates a virtual network topology
2. Switch connects to the Ryu controller
3. Controller registers for port status events
4. When a link changes:

   * Switch sends an event to controller
   * Controller processes the event
   * Logs port state (UP/DOWN)

---

## 🏗️ Project Structure

```
port-status-monitor/
├── port_monitor.py      # Main Ryu controller code
├── README.md            # Project documentation
├── requirements.txt     # Dependencies
```

---

## ▶️ How to Run

### 1. Start Ryu Controller

```
ryu-manager port_monitor.py
```

### 2. Start Mininet

```
sudo mn --topo single,3 --controller remote
```

### 3. Trigger Port Events

```
link s1 h1 down
link s1 h1 up
```

---

## 📊 Sample Output

```
Port 1 is DOWN
Port 1 is UP
```

The controller logs port status changes instantly in the terminal.

---

## 📚 Key Concepts

* Software Defined Networking (SDN)
* Control Plane vs Data Plane
* OpenFlow Protocol
* Event-driven programming
* Network monitoring and fault detection

---

## 🚀 Applications

* Real-time network monitoring
* Fault detection in SDN networks
* Data center infrastructure management
* Network automation systems

---

## 🔮 Future Enhancements

* Store logs in files for analysis
* Add alert/notification system
* Build custom Mininet topologies
* Integrate with visualization dashboards
* Extend to delay and traffic monitoring

---

## 👨‍💻 Author

**Satvik Phadke**

---

## 📌 Conclusion

This project demonstrates how SDN enables centralized control and monitoring of network devices. Using Ryu and Mininet, we can efficiently track network changes and build intelligent monitoring systems.
