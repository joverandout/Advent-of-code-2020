{-# LANGUAGE LambdaCase #-}

module Main where

import Control.Arrow ((&&&))
import Data.List (foldl')

data Compass = N | E | S | W deriving Show
data Relative = F | L | R deriving Show

type Pos = (Int, Int)
data Ship = Ship {position :: Pos, heading :: Compass}
data Command = Command Heading Int deriving Show
data Heading = Absolute Compass | Relative Relative deriving Show
data User = User {boat, marker :: Pos} deriving Show

type Input = [Command]

get :: IO String
get = readFile "input.txt"

rotate :: Relative -> Compass -> Compass
rotate F c = c
rotate L c = case c of
  N -> W
  W -> S
  S -> E
  E -> N
rotate R c = l . l . l $ c
  where l = rotate L

move :: Int -> Compass -> Pos -> Pos
move n d (x, y) = let (dx, dy) = toDelta d
                  in (x + dx * n, y + dy * n)

manVal :: String -> Input
manVal = map parse . lines
  where parse (c:n) = Command d (read n)
          where d = case c of
                      'N' -> Absolute N
                      'S' -> Absolute S
                      'E' -> Absolute E
                      'W' -> Absolute W
                      'F' -> Relative F
                      'R' -> Relative R
                      'L' -> Relative L

follow :: Ship -> Command -> Ship
follow (Ship pos h) (Command t n) = case t of
  Absolute c -> Ship (move n c pos) h
  Relative F -> Ship (move n h pos) h
  Relative r -> Ship pos h'
    where h' = iterate (rotate r) h !! (n `div` 90)

part1 :: Pos -> Int
part1 (x, y) = abs x + abs y

toDelta :: Compass -> Pos
toDelta x = case x of
    N -> (0, 1)
    S -> (0, -1)
    W -> (-1, 0)
    E -> (1, 0)

markerpart2 :: User -> Command -> User
markerpart2 (User pos wp) (Command t n) = case t of
  Absolute c -> User pos (move n c wp)
  Relative F -> User (posCalc n pos wp) wp
  Relative R -> User pos (right wp n 1)
  Relative L -> User pos (right wp n 3)

right :: (Int, Int) -> Int -> Int -> (Int, Int)
right wp n m = iterate turnRight wp !! (n * m)

posCalc :: Int -> (Int, Int) -> (Int, Int) -> (Int, Int)
posCalc n (x,y) (dx, dy) = (x + n * dx, y + n * dy)
        
turnRight :: (Int, Int) -> (Int, Int)
turnRight (x, y) = (y, -x)

main :: IO ()
main = do
       putStrLn "++++++++++++++++"
       putStr   "part 1: "
       get >>= print . (part1 . position . foldl' follow (Ship (0,0) E)) . manVal
       putStr   "part: 2 "
       get >>= print . (part1 . boat .foldl' markerpart2 (User (0, 0) (10, 1))) . manVal
       putStrLn "++++++++++++++++"
