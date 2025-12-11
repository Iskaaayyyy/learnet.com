# LearnNet Content Seeding Guide

## Overview

This guide explains how to seed the LearnNet database with networking educational content.

## Quick Start

1. **Run the seeding script:**
   ```bash
   cd backend
   python seed_networking_content.py
   ```

2. **Verify the content:**
   - Login as admin
   - Check that the "Complete Networking Fundamentals" course exists
   - Verify modules and lessons are created

## Current Content Structure

The seeding script creates:

- **1 Main Course**: "Complete Networking Fundamentals"
- **Multiple Modules**: Organized by topic
- **Lessons per Module**: 5-10 lessons each
- **Quizzes**: One quiz per lesson with 5-7 questions

## Adding More Content

### Option 1: Extend the Seeding Script

Edit `backend/seed_networking_content.py` and add more modules/lessons to the `modules_data` list.

### Option 2: Use the Web Interface

1. Login as instructor (or admin)
2. Create courses, modules, and lessons through the web interface
3. Add quizzes for each lesson

### Option 3: Database Direct Insert

For bulk content, you can write custom scripts to insert directly into the database.

## Content Guidelines

When adding networking lessons:

1. **Follow a logical progression**: Beginner → Intermediate → Advanced
2. **Include clear explanations**: Student-friendly language
3. **Add key concepts**: Highlight important points
4. **Provide summaries**: Help students review
5. **Create quizzes**: 5-10 questions per lesson
6. **Use real-world examples**: Make content practical

## Topics to Cover (100 Lessons Target)

### Foundation (Lessons 1-20)
- Network basics
- OSI/TCP-IP models
- Network devices
- Cabling and physical layer
- Topologies

### Protocols (Lessons 21-40)
- Ethernet
- IP addressing
- Subnetting
- TCP/UDP
- DNS, DHCP
- ARP

### Routing & Switching (Lessons 41-60)
- Router configuration
- Switch configuration
- VLANs
- Routing protocols (RIP, OSPF, EIGRP)
- STP

### Security (Lessons 61-75)
- Firewalls
- VPNs
- Wireless security
- Access control
- Threats and mitigation

### Advanced Topics (Lessons 76-100)
- Network troubleshooting
- Monitoring and management
- Cloud networking
- IPv6
- Network design

## Notes

- The seeding script checks if content already exists to avoid duplicates
- You can run it multiple times safely
- To reset, delete the database file and recreate

