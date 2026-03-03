# Configura o provedor do Google Cloud usando sua chave
provider "google" {
  credentials = file("chave.json")
  project     = "project-d101fdb9-1c3d-414f-867" # Este é o ID que aparece no seu console
  region      = "us-central1"
  zone        = "us-central1-a"
}

# Cria uma máquina virtual (servidor) gratuita
resource "google_compute_instance" "vm_victor" {
  name         = "servidor-v2"
  machine_type = "e2-micro" # Tipo que entra no free tier

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {
      # Isso aqui dá um endereço de internet para a máquina
    }
  }
}