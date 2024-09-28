def benoulli_numbers(tedad):
    benoulli_list = [1]
    for m in range (1 , tedad + 1):
        benoulli_list . append(0)
        for j in range(m ,0, -1):
            benoulli_list[j - 1] = j * (benoulli_list[j - 1] - benoulli_list[j] )
        return benoulli_list
tedad = int(input("tedad adad donbahe bernoulli ra vared kon:"))
benoulli_sequence = benoulli_numbers(tedad)
print("donbale bernoulli ta adad" , tedad ,"ebarat ast az:")
print(benoulli_sequence)