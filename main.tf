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

# --- ADICIONE ESTE BLOCO ABAIXO ---
# Esse código vai fazer o IP aparecer em verde no seu terminal
output "ip_externo_servidor" {
  value       = google_compute_instance.vm_victor.network_interface[0].access_config[0].nat_ip
  description = "Use este IP no campo 'Servidor' do Power BI"
}