(define (deep-reverse x)
  (cond [(null? x) '()]
        [(pair? (car x))(append (deep-reverse (cdr x))(list (deep-reverse (car x))))]
        [else(append (deep-reverse (cdr x))(list (car x)))]) )


(deep-reverse '())
()
(reverse '(1 (2 3) 4 5))
(deep-reverse '(1 (2 3) 4 5))
(reverse '(1 (2 3) (4 (5 6) 7) (8 9 (10 11 (12)))))
(deep-reverse '(1 (2 3) (4 (5 6) 7) (8 9 (10 11 (12)))))


(define viterbiProb
  (emission k switchPr p1 p2)
  (cond[(null? (cdr emission))
        1]
       [(
         (let ((two_pairs (loop (cdr emission) (- k 1) switchPr p1 p2)) ;gets two pairs of F or B paired with their probabilities
               (most_likely (max(two_pairs))) ;gets the most likely last coin 
               (second_likely (if (= most_likely (car two_pairs) (car (cdr two_pairs)) (car two_pairs)))) ;gets second likely coin with its probability
               (is_ml_p1 (if ( = (car most_likely) p1) #t #f))  ;Is Most likely p1 or not?
               (is_inverse (if ( = (car emission) 1) #f #t)) ; is it 0 or not
               (c_p1 (- 1 p1))
               (c_p2 (- 1 p2))) ; return the complement of the probability
         (cons 
               ( (if (is_ml_p1)
                     (pair p1 (car (cdr ((max
                                          (
                                           (* (car (cdr second_likely)) switchPr (if (is_inverse) c_p2 p2)) ; V(B) x switching x (inverse or not of p2, depending on the emission)
                                           (* (car (cdr most_likely)) (- 1 switchPr) (if (is_inverse) c_p1 p1)) ; V(F) x not_switching x (inverse or not of p1, d on em)
                                           )

                                          )))))
                     (pair p1 (car (cdr ((max(
                                              (* (car (cdr second_likely)) (- 1 switchPr) (if (is_inverse) c_p1 p1)) ; V(F) x not_switching x (inverse or not of p1, d on em)
                                              (* (car (cdr most_likely)) switchPr  (if (is_inverse) c_p2 p2))))))))) ;V(B) x switching x (inverse or not of p2, depending on the emission)
                     ))
                 ;;Where do I pass on the inverse probabilites? FUUUU
               (pair (p2 ( max(* ())
                             (* () ) ) ))))))
         )]
;Max of (Viterbi(k-1, p1)*switchPr*p1,
   ;     Vitervi(k-1, p2)*(1-switchPr)*p1)
   ))
