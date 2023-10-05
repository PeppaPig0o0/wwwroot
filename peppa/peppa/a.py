def test(a, **kwargs):
    print(a,kwargs)



dic = {
    'm':123,
    'n':456,

}
test(2,m=1,n=2,c=3)
