#!/usr/bin/env bash
gcloud compute instances create myinstance --machine-type=n1-standard-1 --zone=us-central1-a  
gcloud compute firewall-rules create allow-winrm --allow tcp:8080