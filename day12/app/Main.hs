{-# LANGUAGE LambdaCase #-}

module Main where

import Control.Arrow ((&&&))
import Data.List (foldl')

type Pos = (Int, Int)
data Compass = N | E | S | W deriving Show
data Relative = F | L | R deriving Show
data Ship = Ship {position :: Pos, heading :: Compass}
data Instruction = Instruction Heading Int deriving Show
data Heading = Absolute Compass | Relative Relative deriving Show
data Traveler = Traveler {boat, marker :: Pos} deriving Show

type Input = [Instruction]

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
  where parse (c:n) = Instruction d (read n)
          where d = case c of
                      'N' -> Absolute N
                      'S' -> Absolute S
                      'E' -> Absolute E
                      'W' -> Absolute W
                      'F' -> Relative F
                      'R' -> Relative R
                      'L' -> Relative L

follow :: Ship -> Instruction -> Ship
follow (Ship pos h) (Instruction t n) = case t of
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

markerpart2 :: Traveler -> Instruction -> Traveler
markerpart2 (Traveler pos wp) (Instruction t n) = case t of
  Absolute c -> Traveler pos (move n c wp)
  Relative F -> Traveler pos' wp
    where pos' = let (x, y) = pos
                     (dx, dy) = wp
                 in (x + n * dx, y + n * dy)
  Relative R -> Traveler pos (right wp n 1)
  Relative L -> Traveler pos (right wp n 3)

right :: (Int, Int) -> Int -> Int -> (Int, Int)
right wp n m = iterate turnRight wp !! (n * m)
        
turnRight :: (Int, Int) -> (Int, Int)
turnRight (x, y) = (y, -x)

main :: IO ()
main = do
       putStrLn "++++++++++++++++"
       putStr "part 1: "
       get >>= print . (part1 . position . foldl' follow (Ship (0,0) E)) . manVal
       putStr "part: 2 "
       get >>= print . (part1 . boat .foldl' markerpart2 (Traveler (0, 0) (10, 1))) . manVal
       putStrLn "++++++++++++++++"
