import torch

def train_model(model, loader, criterion, optimizer, device, epoch):
    model.train()
    total_loss = 0

    for data in loader:
        data = data.to(device)
        optimizer.zero_grad()
        output = model(data).squeeze()  # Shape: (batch_size, n_nodes, n_classes)
        target = data.y.to(device).squeeze()  # Shape: (batch_size, n_nodes)

        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        total_loss += loss.item() * data.num_graphs
        torch.save(model.state_dict(), 'checkpoints/model_size_epoch_{epoch}.pth'.format(epoch=epoch+1))

    return total_loss / len(loader.dataset)

