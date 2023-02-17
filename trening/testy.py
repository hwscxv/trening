def is_adult(age: int) -> bool:    #age = int    is_adult = true/false!!
    return age >= 18



def test_is_adult():
    #given
    age = 18

    #when
    result = is_adult(age)

    #then  
    assert result                   #assert -> result true = ok, result false not ok (szczegolne przypadki)
    assert is_adult(20)


def test_is_not_adult():
    assert not is_adult(17)
    assert not is_adult(3)