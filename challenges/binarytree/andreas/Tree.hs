module Tree ( Tree(..)
            , insert
            , fromList
            , toList
            , lookup
            ) where

import Prelude hiding (lookup)


data Tree k a = EmptyNode | Node k a (Tree k a) (Tree k a) deriving (Show)


insert :: Ord k => k -> a -> Tree k a -> Tree k a
insert key value EmptyNode = Node key value EmptyNode EmptyNode
insert key value (Node k v left right)
    | key == k = Node k value left right
    | key <  k = Node k v (insert key value left) right
    | key >  k = Node k v left (insert key value right)

fromList :: Ord k => [(k,a)] -> Tree k a
fromList = foldr (\ (k,v) -> insert k v) EmptyNode

toList :: Tree k a -> [(k, a)]
toList EmptyNode = []
toList (Node k v left right) = toList left ++ [(k, v)] ++ toList right

lookup :: Ord k => k -> Tree k a -> Maybe a
lookup _ EmptyNode = Nothing
lookup key (Node k v left right)
    | key == k = Just v
    | key <  k = lookup key left
    | key >  k = lookup key right
