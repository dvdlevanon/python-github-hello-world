#!/bin/bash

eksctl create cluster --name david-test2 --nodes=1 --ssh-access --ssh-public-key david-test-key

aws eks update-kubeconfig --kubeconfig kubeconfig --name david-test2
