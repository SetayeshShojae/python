def benoulli_numbers(tedad):
    benoulli_list = [1]
    for d in range (1 , tedad + 1):
        benoulli_list . append(0)
        for s in range(d ,0, -1):
            benoulli_list[s - 1] = j * (benoulli_list[s - 1] - benoulli_list[s] )
        return benoulli_list
tedad = int(input("tedad adad donbahe bernoulli ra vared kon:"))
benoulli_sequence = benoulli_numbers(tedad)
print("donbale bernoulli ta adad" , tedad ,"ebarat ast az:")
print(benoulli_sequence)