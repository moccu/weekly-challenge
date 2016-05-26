import Test.HUnit
import Prelude hiding (lookup)

import Tree


main = runTestTT $ TestList [ testInsert
                            , testFromList
                            , testLookup
                            , testToList
                            ]


testInsert :: Test
testInsert = TestCase $ do
    let t1 = insert 3 "c" EmptyNode
        t2 = insert 1 "a" t1
        t3 = insert 4 "d" t1
    (Node 3 "c" EmptyNode EmptyNode) @=? t1
    (Node 3 "c" (Node 1 "a" EmptyNode EmptyNode) EmptyNode) @=? t2
    (Node 3 "c" EmptyNode (Node 4 "d" EmptyNode EmptyNode)) @=? t3
    let t4 = insert 3 "x" t1
    (Node 3 "x" EmptyNode EmptyNode) @=? t4

testFromList :: Test
testFromList = TestCase $ do
    let t1 = fromList [(3,"c"), (2,"b")]
    (Node 3 "c" (Node 2 "b" EmptyNode EmptyNode) EmptyNode) @=? t1

testLookup :: Test
testLookup = TestCase $ do
    let t1 = (Node 2 "b" (Node 1 "a" EmptyNode EmptyNode) EmptyNode)
        t2 = (Node 2 "b" EmptyNode (Node 3 "c" EmptyNode EmptyNode))
    Nothing @=? (lookup 0 t1)
    (Just "b") @=? (lookup 2 t1)
    (Just "a") @=? (lookup 1 t1)
    (Just "c") @=? (lookup 3 t2)

testToList :: Test
testToList = TestCase $ do
    let t1 = (Node 2 "b" (Node 1 "a" EmptyNode EmptyNode) EmptyNode)
        t2 = (Node 2 "b" EmptyNode (Node 3 "c" EmptyNode EmptyNode))
    [(1,"a"), (2,"b")] @=? (toList t1)
    [(2,"b"), (3,"c")] @=? (toList t2)
