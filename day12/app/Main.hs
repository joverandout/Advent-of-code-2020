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

type Input = [Instruction]

turn :: Relative -> Compass -> Compass
turn F c = c
turn L c = case c of
  N -> W
  W -> S
  S -> E
  E -> N
turn R c = l . l . l $ c
  where l = turn L

move :: Int -> Compass -> Pos -> Pos
move n d (x, y) = let (dx, dy) = toDelta d
                  in (x + dx * n, y + dy * n)

follow :: Ship -> Instruction -> Ship
follow (Ship pos h) (Instruction t n) = case t of
  Absolute c -> Ship (move n c pos) h
  Relative F -> Ship (move n h pos) h
  Relative r -> Ship pos h'
    where h' = iterate (turn r) h !! (n `div` 90)

manhattan :: Pos -> Int
manhattan (x, y) = abs x + abs y

toDelta :: Compass -> Pos
toDelta x = case x of
  N -> (0, 1)
  S -> (0, -1)
  W -> (-1, 0)
  E -> (1, 0)

prepare :: String -> Input
prepare = map parse . lines
  where parse (c:n) = Instruction d (read n)
          where d = case c of
                      'N' -> Absolute N
                      'S' -> Absolute S
                      'E' -> Absolute E
                      'W' -> Absolute W
                      'F' -> Relative F
                      'R' -> Relative R
                      'L' -> Relative L

main :: IO ()
main = readFile "input.txt" >>= print . (manhattan . position . foldl' follow (Ship (0,0) E)) . prepare